// 1. ncmbモジュールの読み込み
var NCMB = require("ncmb");

// 2. mobile backendアプリとの連携
var ncmb = new NCMB(
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
);

// 送信テキストの取得
var msg = process.argv[2];

// TestClassの作成
var RaspiotClass = ncmb.DataStore("RaspiotClass");
// 3.TestClassへの入出力
RaspiotClass.equalTo("message", msg)
         .fetchAll()
         .then(function(results){
           if(results[0] != null){
             console.log(results[0].get("message"));
           }else{
             var raspiotClass = new RaspiotClass();
             raspiotClass.set("message", msg);
             raspiotClass.save()
                      .then(function(){
                        console.log("message is saved.");
                      })
                      .catch(function(err){
                        console.log(err.text);
                      });
           }
         })
         .catch(function(err){
           console.log(err.text);
         });
