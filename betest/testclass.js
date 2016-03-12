// 1. ncmbモジュールの読み込み
var NCMB = require("ncmb");

// 2. mobile backendアプリとの連携
var ncmb = new NCMB(
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
);

// TestClassの作成
var TestClass = ncmb.DataStore("TestClass");
// 3.TestClassへの入出力
TestClass.equalTo("message", "Hello, NCMB!")
         .fetchAll()
         .then(function(results){
           if(results[0] != null){
             console.log(results[0].get("message"));
           }else{
             var testClass = new TestClass();
             testClass.set("message", "Hello, NCMB!");
             testClass.save()
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
