'use strict';

const Singleton = function(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

Object.defineProperty(Singleton.prototype, 'fullname', {
  get: function() {
    return `${this.firstName} ${this.lastName}`;
   }
})

Singleton.prototype.fullName =  ()=> {
  return this.fullname;
}

let object = new Singleton('First', 'Last');
console.log(object.fullName());
