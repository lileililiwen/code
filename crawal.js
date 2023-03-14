const request = require('request');
const cheerio = require('cheerio');

const url = 'https://www.656463.com/wenda?page='; // 列表页URL
const maxPages = 5; // 最大爬取页数

let currentPage = 1;

const selector = ' div.main_left   ul   li'; // 选择器，用于选择要提取的元素


function crawlPage(page) {
  const pageUrl = url + page;
  console.log("apgeUrl:"+pageUrl)
  request(pageUrl, (error, response, html) => {
      console.log("bbbbbbbbbb"+response.statusCode)
    if (!error && response.statusCode === 200) {
      const $ = cheerio.load(html);

      $(selector).each((i, el) => {
        const link = $(el).attr('href'); // 获取元素链接
        // request(link, (error, response, html) => {
        //   if (!error && response.statusCode === 200) {
        //     const $ = cheerio.load(html);

        //     // 在这里提取想要的数据
        //     const title = $('.tw_li_title a').text();
        //     //const content = $('article').html();
        //     console.log("aaaaaaaaa"+title);
        //   }
        // });
        // 在这里提取想要的数据
        const title = $(el).find('.tw_li_title a').text();
        //const content = $('article').html();
        console.log("aaaaaaaaa"+title);
      });
      
      // 继续爬取下一页
      if (page < maxPages) {
        crawlPage(page + 1);
      }
    }
  });
}

crawlPage(currentPage);