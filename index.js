import { Douyu } from 'lsar/dist/apis/douyu/index.js'
import fs from 'fs'

const flvUrlRegex = /(https?:\/\/[^ ]*).flv/;
const m3u8UrlRegex = /(https?:\/\/[^ ]*).m3u8/;
const urlList = [];
console.log = function (d) {
    const msg = d.toString()
    if (msg.match(flvUrlRegex) && msg.match(flvUrlRegex)[0]) {
        urlList.push(msg.match(flvUrlRegex)[0]);
    }
    if (msg.match(m3u8UrlRegex) && msg.match(m3u8UrlRegex)[0]) {
        urlList.push(msg.match(m3u8UrlRegex)[0]);
    }
    process.stdout.write(d + '\n');
};

new Douyu(74751).printLiveLink()
    .then(() => {
        const playList = "#EXTM3U" + urlList.map((url, index) => `\n#EXTINF:-1, Source(${index})\n${url}`);
        fs.writeFile('./playlist.m3u8', playList, function (err) {
            if (err) throw err;
            console.log('File is created successfully.');
        });
    })
    .catch((e) => {
        console.log(e)
    });