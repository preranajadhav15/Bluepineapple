const fetch=require("node-fetch");
async function fetchData() {
    try{
        const result=await new Promise((resolve,reject)=> {
            setTimeout(()=> {
                const success=true
                if(success) resolve("data fetch successfully")
                else reject("failed to fetch data")
            },2000)
        });
        console.log(result);
    } catch (error) {
        console.error(error)
    }
    
}
fetchData();

async function getPosts() {
    try {
        const response=await fetch("http://jsonplaceholder.typicode.com/posts")
        const posts =await response.json();
        console.log("\nfirst 5 posts:")
        posts.slice(0,5).forEach((post,index)=> {
            console.log(`post ${index+1}:`)
            console.log("Title:",post.title)
            console.log("body:",post.body)
        });
    } catch (error) {
        console.error(error)
    }
}
getPosts();

async function fetchMultipleEndpoints() {
    try {
        const[postsRes,commentsRes]=await Promise.all([
            fetch("http://jsonplaceholder.typicode.com/posts"),
            fetch("https://jsonplaceholder.typicode.com/comments"),
        ]);
        const posts=await postsRes.json();
        const comments=await commentsRes.json();
        console.log("\nnumber of posts fetched:",posts.length);
        console.log("number of comments fetched:",comments.length);
    } catch (error) {
        console.error("error fetching multiple endpoints:",error);
    }
}
fetchMultipleEndpoints();
