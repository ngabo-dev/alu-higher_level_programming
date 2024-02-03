#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    } else {
      // Create an instance with width and height set to undefined
      return new Rectangle();
    }
  }
}

module.exports = Rectangle;
