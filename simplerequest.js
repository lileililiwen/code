//利用request来访问页面，利用cherro来解析页面
const request = require('request');
const cheerio = require('cheerio');

const url = 'https://www.baidu.com';

request(url, function(error, response, body) {
  if (!error && response.statusCode == 200) {
    const $ = cheerio.load(body);
    $('a').each(function() {
      const link = $(this).attr('href');
      console.log("aaaaaa"+link);
    });
  } else {
    console.log('Error:', error);
  }
});
