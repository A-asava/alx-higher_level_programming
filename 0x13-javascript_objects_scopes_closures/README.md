JavaScript - Objects, Scopes and Closures

Objects in JavaScript:
Objects are a fundamental data structure in JavaScript that allows you to group related data and functions together. They are key-value pairs, where each value can be a primitive type, another object, or a function. Objects are created using curly braces {} and can be dynamically modified.

EXAMPLE OF AN OBJECT:

// Creating an object const person = { name: 'John', age: 30, greet: function() { console.log('Hello, ' + this.name + '!'); } };

// Accessing object properties console.log(person.name); // Output: John

// Calling a method person.greet(); // Output: Hello, John!

Scopes in JavaScript:
Scope in JavaScript refers to the context in which variables and functions are declared and accessed

Closures in JavaScript:
A closure is formed when a function is defined inside another function, allowing the inner function to access the outer function's variables and parameters even after the outer function has finished executing. Closures provide a way to create private variables and encapsulate functionality.

EXAMPLE OF A CLOSURE IN JAVASCRIPT:

function outerFunction(x) { // Inner function has access to outer function's parameter function innerFunction(y) { return x + y; } return innerFunction; }

const closureExample = outerFunction(5); console.log(closureExample(3)); // Output: 8
