#!/usr/bin/env node

var os = require('os');
var irc = require('irc');
var http = require('http');

var join_allow_channels = [
  '#pgonee_world'
];
var client = new irc.Client('irc.ntspot.co.kr', 'pgonee_server', {
  channels: join_allow_channels
});

client.addListener('pm', function(from, message) {
  console.log('(Private message) ' + from + ' -> ' + message); 
});

client.addListener('message', function(from, to, message) {
  if (join_allow_channels.indexOf(to) > -1) {
    
    /*
     * FIX_ME: 인코딩 문제
     *var buf = new Buffer(message, 'cp949');
     *message = buf.toString();
     */
    console.log('(' + to + ') ' + from + ' -> ' + message);

    if (message.length) {
      if (message[0] == '@') {
        var split = message.split('@');
        if (split.length >= 2) {
          var cmd = split[1];
          if (cmd == 'ipconfig') {
            console.log('[+] ipconfig');
            client.say(to, ipconfig());
          } else if (cmd == 'external_ipconfig') {
            console.log('[+] external_ipconfig');
            external_ipconfig(function(address) {
              client.say(to, address);
            });
          }
        }
      }
    }
  }
});

var ipconfig = function() {
  var ninfo = os.networkInterfaces();
  var rst = '';
  
  for(var k in ninfo) {
    var v = ninfo[k];
    rst += k + ' { ';

    for(var kk in v) {
      var vv = v[kk];
      if (vv.family == 'IPv4') {
        rst += vv.address + ','; 
      }
    }

    rst += ' }, ';
  };

  return rst;
};

var external_ipconfig = function(cb) {
  http.get('http://ipconfig.co.kr', function(res) {
    res.on('data', function(data) {
      var rst = data.toString();
      var rst2 = [];
      var tmp = rst.match(/\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b/);
      cb(tmp[0]);
    });
  });
};
