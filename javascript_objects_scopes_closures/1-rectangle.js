#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Initialize the instance attributes width and height
    this.width = w;
    this.height = h;
  }
}
const myRectangle = new Rectangle(10, 5);
console.log(myRectangle.width);
console.log(myRectangle.height);
