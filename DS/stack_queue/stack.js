class Stack {
  constructor() {
    this.stack = [];
  }
  push(item) {
    this.stack.push(item);
  }
  pop() {
    return this.stack.pop();
  }
  size() {
    return this.stack.length;
  }
  peek() {
    return this.stack[this.size() - 1];
  }
  isEmpty() {
    return this.stack.length === 0 ? true : false;
  }
}

const stack = new Stack();

stack.push(1);
stack.push(2);

console.log(stack.size());
console.log(stack.peek());
console.log(stack.pop());
console.log(stack.size());
console.log(stack.isEmpty());
console.log(stack.pop());
console.log(stack.isEmpty());
