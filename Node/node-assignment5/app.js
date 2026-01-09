const express=require("express");
const fetch=require("node-fetch");
const app=express();
const PORT=3000;

app.use(express.json());
app.use((req,res,next)=>{
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});
app.get("/",(req,res)=> {
    res.send("welcome to express");
});

app.post("/data",(req,res)=> {
    const receivedData=req.body;
    console.log("received data:",receivedData);
    res.send("data received");
});

app.get("/users",(req,res)=>{
    const users=[
        {id:1,name:"Ayan"},
        {id:2,name:"Riya"},
        {id:3,name:"Isha"},
    ];
    res.json(users);
});
app.get("/externalposts",async(req,res)=> {
    try {
        const response=await fetch("https://jsonplaceholder.typicode.com/posts");
        const posts=await response.json();
        res.json(posts);
    } catch (error) {
        console.error("error fetching external posts:",error);
        res.status(500).send("failed to fetch external posts");
    }
});
app.use((req,res)=> {
    res.status(404).send("404 not found: the route you requested does not exist");
});
app.use((err,req,res,next)=> {
    console.error("server error:",err);
    res.status(500).send("something went wrong");
});
app.listen(PORT,()=> {
    console.log(`server running at http://localhost:${PORT}`);
});

