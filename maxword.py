function maxlength(data: string): void {

console.log(data)
let long_word, max_word : string
let max = 0

const revised_data = data.split(' ')
const rev_len = revised_data.length
console.log(rev_len)

for (let i=0; i<rev_len; i++) {
    let length = revised_data[i].length
    if (length > max) {
        max_word = revised_data[i]
        max = length
    }
}
console.log(max_word)
 
}

maxlength('i love india')
