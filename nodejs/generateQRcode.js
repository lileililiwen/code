const QRCode = require('qrcode')
const { createCanvas, loadImage } = require('canvas')
const fs = require('fs')

async function generateQRCode(text, type, options) {
  const canvasSize = options.canvasSize || 400
  const padding = options.padding || 10
  const bgColor = options.bgColor || '#ffffff'
  const fgColor = options.fgColor || '#000000'
  const borderColor = options.borderColor || '#000000'
  const innerBorderColor = options.innerBorderColor || '#000000'

  let data
  switch (type) {
    case 'text':
      data = text
      break
    case 'tel':
      data = `tel:${text}`
      break
    case 'sms':
      data = `sms:${text}`
      break
    case 'vcard':
      const [name, phone, company, url, title, email, address] = text.split('|')
      data = `BEGIN:VCARD\nVERSION:3.0\nFN:${name}\nORG:${company}\nTITLE:${title}\nTEL;TYPE=WORK,VOICE:${phone}\nADR;TYPE=WORK:${address}\nEMAIL:${email}\nURL:${url}\nEND:VCARD`
      break
    case 'url':
      data = text
      break
    case 'wifi':
      const [ssid, password, security] = text.split('|')
      data = `WIFI:T:${security};S:${ssid};P:${password};;`
      break
    default:
      throw new Error('Unsupported type')
  }

  const canvas = createCanvas(canvasSize, canvasSize)
  const context = canvas.getContext('2d')

  context.fillStyle = bgColor
  context.fillRect(0, 0, canvasSize, canvasSize)

  const qrCodeOptions = {
    margin: 1,
    color: {
      dark: fgColor,
      light: bgColor
    },
    errorCorrectionLevel: 'H'
  }

  const qrCodeData = await QRCode.toDataURL(data, qrCodeOptions)

  const qrCodeImage = await loadImage(qrCodeData)
  context.drawImage(qrCodeImage, padding, padding, canvasSize - padding * 2, canvasSize - padding * 2)

  context.strokeStyle = borderColor
  context.lineWidth = 4
  context.strokeRect(0, 0, canvasSize, canvasSize)

  context.strokeStyle = innerBorderColor
  context.lineWidth = 2
  context.strokeRect(padding, padding, canvasSize - padding * 2, canvasSize - padding * 2)

  const fileName = `${type}_${Date.now()}.png`
  const stream = canvas.createPNGStream()
  const writeStream = fs.createWriteStream(fileName)
  stream.pipe(writeStream)
  return new Promise(resolve => {
    writeStream.on('finish', () => resolve(fileName))
  })
}

(async () => {
  const options = {
    canvasSize: 500,
    padding: 20,
    bgColor: '#ffffff',
    fgColor: '#000000',
    borderColor: '#000000',
    innerBorderColor: '#000000'
  }
  const type = 'text'
  const text = 'Hello World!'
  try {
    const fileName = await generateQRCode(text, type, options)
    console.log("Generated QR code: ${fileName}")
  } catch (error) {
    console.error(error)
  } 
})()
