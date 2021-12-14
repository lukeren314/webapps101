console.log("hello world"); // notice the semi colon
// you can also use single quotes

// this is a comment
let num = 0;
console.log(num);

num = num + 1;
num++;
num += num;
console.log(num);

let bool = true || false && true;
console.log(num+"bob"+bool);

let fstring = `1 + 2 = ${1 + 2}`; // f'1 + 2 = ${1 + 2}' in Python
console.log(fstring);

if (num == 0) {
    console.log(0);
} else if (num == 1) {
    console.log(1);
} else {
    console.log(2);
}

let list = [1, 2, 3];
console.log(list[0]);

list.push(4);
console.log(list);
list.pop();
console.log(list);
// for more list functions, look up JavaScript Array

let i = 0;
while(i < 10) {
    console.log(i);
    i++;
}

for (let i = 0; i < 10; i++) {
    console.log(i);
}

for (let i of list) {
    console.log(i);
}

// you don't need quotes around the keys
let dict = {
    foo: "a",
    bar: "b"
};

// two ways to access a value in a dictionary
console.log(dict.foo);
console.log(dict["foo"]);

for (let key in dict) {
    console.log(key);
    console.log(dict[key]);
}

// you can desctructure lists and dictionaries
let [a, b, c] = [1, 2, 3];
let {foo, bar} = dict;

// you can also pass multiple values into consoe.log
console.log(a, b, c);
console.log(foo, bar);

function add(a, b) {
    return a + b;
}

console.log(add(1, 2));

let storedAdd = add;
console.log(storedAdd(1, 2));

// you can also define lambda functions, called arrow functions in JavaScript
let addTwoNumbers = (a, b) => a + b;

// something you can't do in python is have a multiline lambda function
let addThreeNumbers = (a, b, c) => {
    let total = 0;
    total += a;
    total += b;
    total += c;
    return total;
};

class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(this.name + " makes a noise.");
    }
}

let dog = new Animal("dog");
dog.speak();