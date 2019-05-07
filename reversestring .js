// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {



    return str.split('').reduce((reversed, char) => char + reversed)
    // let reversed = "";
    // for (let char of str) {
    //     reversed = char + reversed;
    // }
    // return reversed
    // var arr1 = [...str];
    // var arr2 = [];
    // for (var i = arr1.length; i > 0; i--) {

    //     arr2.push(arr1[i - 1])

    // }
    // return arr2.join('')
    // return str.split('').reverse().join('')

}


module.exports = reverse;