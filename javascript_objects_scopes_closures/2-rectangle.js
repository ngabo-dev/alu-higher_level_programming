#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    } else {
      // Return an empty object if conditions are not met
      return {};
    }
  }
}

module.exports = Rectangle;
