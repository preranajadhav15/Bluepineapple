class Calculator {
    constructor() {
        this.value=0;
    }
    add(num) {
        this.value+=num;
        return this;
    }
    subtract(num) {
        this.value-=num;
        return this;
    }
    multiply(num) {
        this.value*=num;
        return this;
    }
    divide(num) {
        if(num==0){
            console.log("cannot divided by zero");
            return this
        }
        this.value/=num;
        return this;
    }
    getResult() {
        return this.value;
    }
}
const cal= new Calculator();
const result=cal.add(5).subtract(2).multiply(3).divide(2).getResult();
console.log("Result:",result);

function fetchData() {
    return new Promise((resolve,reject)=> {
        setTimeout(()=>{
            const success=true;
            if(success){
                resolve("data fetched successfully")
            } else {
                reject("failed to fetch data")
            }
        },2000);
    });
}

fetchData()
.then((data)=>{
    console.log(data);
})
.catch((error)=>{
    console.error(error);
})
