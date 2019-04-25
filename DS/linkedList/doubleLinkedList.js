class Node {
  constructor(data) {
    this.prev = null;
    this.next = null;
    this.data = data;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  display() {
    let node = this.head;
    const elem = [];
    while (node !== null) {
      elem.push(node.data);
      node = node.next;
    }
    return elem.join(', ');
  }

  append(data) {
    const newNode = new Node(data);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.prev = this.tail;
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  appendAt(pos, data) {
    let count = 0;
    let node = this.head;

    while (count !== pos) {
      node = node.next;
      count += 1;
    }

    const newNode = new Node(data);

    if (pos === 0) {
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    } else {
      node.prev.next = newNode;
      newNode.next = node;
    }
  }

  remove(data) {
    let node = this.head;
    while (node.data !== data) {
      node = node.next;
    }
    this.deleteNode(node);
  }

  removeAt(pos) {
    let count = 0;
    let node = this.head;

    while (count !== pos) {
      node = node.next;
      count += 1;
    }

    this.deleteNode(node);
  }

  deleteNode(node) {
    if (node === this.head && node === this.tail) {
      this.head = null;
      this.tail = null;
    } else if (node === this.head) {
      this.head = node.next;
      node.next.prev = null;
    } else if (node === this.tail) {
      this.tail = node.prev;
      node.prev.next = null;
    } else {
      node.prev.next = node.next;
      node.next.prev = node.prev;
    }
  }

  reverse() {
    let node = this.tail;
    this.node = this.head;
    this.head = node;
    let prev = null;

    while (node !== null) {
      let next = node.prev;
      node.next = next;
      node.prev = prev;
      prev = node;
      node = node.next;
    }
  }
}

const linkedList = new LinkedList();
linkedList.append(1);
linkedList.append(10);
linkedList.append(100);
linkedList.append(30);

console.dir(linkedList.display());
// linkedList.appendAt(0, 40);
// console.dir(linkedList.display());
// linkedList.remove(100);
// console.dir(linkedList.display());
// linkedList.remove(40);
// // linkedList.remove(30);
// console.dir(linkedList.display());
// linkedList.removeAt(1);
// console.dir(linkedList.display());
linkedList.reverse();
console.dir(linkedList.display());
