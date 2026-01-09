const http=require("http")
const helper=require("./helper")
console.log(helper.getMessage())
const server=http.createServer((req,res)=> {
    res.writeHead(200,{"content-type":"text/plain"})
    res.end("welcome to node.js!")
});
server.listen(3000,()=>{
    console.log("Server is running on http://localhost:3000")
});


