let arr = [];
for (let i = 0; i < 10; i++) {
    arr.push(Math.floor(Math.random() * 100) + 1);
}
console.log("Array:", arr);

function min_max_avg(arr) {
    let maximum = Math.max(...arr); 
    let minimum = Math.min(...arr);

    let sum = arr.reduce((total, num) => total + num, 0);
    let average = sum / arr.length;

    console.log("Largest number:", maximum);
    console.log("Smallest number:", minimum);
    console.log("Average:", average.toFixed(2));
}

min_max_avg(arr);
