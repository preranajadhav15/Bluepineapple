const fs=require("fs")
console.log("program start")
if(!fs.existsSync("log.txt")) {
    fs.writeFileSync("log.txt","This is a log file.\n")
}
fs.appendFileSync("log.txt","New log added on run.\n")
console.log("File created successfilly")
function readFileBlocking() {
    console.log("Blocking read started")
    const data=fs.readFileSync("log.txt","utf8")
    console.log("Blocking read content:")
    console.log(data)
    console.log("Blocking read finished")
}
readFileBlocking();

function readFileNonBlocking() {
    console.log("non-blocking read started")
    fs.readFile("log.txt","utf8",(err,data)=> {
        if(err) {
            console.error(err);
            return;
        }
        console.log("non-blocking read content:")
        console.log(data);
    });
}
readFileNonBlocking();

process.nextTick(()=> {
    console.log("process.nextTick executed")
});
setTimeout(()=> {
    console.log("setTimeout executed")
},0);
setImmediate(()=> {
    console.log("setImmediate executed")
});
console.log("program end")
