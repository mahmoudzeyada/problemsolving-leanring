//  function Dog(name, breed) {
//      var new_dog = this;
//      new_dog.name = name;
//      new_dog.breed = breed;
//      new_dog.hoo = function hoo() {
//          console.log(new_dog.breed);
//      }

//  }

//  var snoopy = new Dog('Snoopy', "Beagle");

//  // var lassie = new Dog('Lassie', 'Collie');
//  console.log(snoopy.__proto__)
//  console.log(Dog.__proto__)

// console.log(snoopy.breed);
// console.log(Function.__proto__)
// snoopy.hoo();

// var lassie = {
//     name: 'lassie',
//     breed: 'hooo',
//     speak: function () {
//         return 'Woof woof';
//     }
// };

// var snoopy = {};
// snoopy.speak = lassie.speak;
// console.log(snoopy["speak"].__proto__);
var Dog = function () {
    this.name = "mahmoud"
}

snoopy = Object.create(Dog)
console.log(snoopy.prototype)
console.log(snoopy.__proto__)

console.log(Dog.prototype)
console.log(Dog.__proto__)