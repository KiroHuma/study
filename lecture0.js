// 1  Pick up phone book
function findPerson(contacts, personName){
    let left = 0;
    let right = contacts.length - 1;

// 2  Open to middle of phone book
while (left <= right){
    let middle = Math.floor((left + right) / 2);

// 3  Look at page
let currentPage = contacts[middle];
// 4  If person is on page
if (currentPage === personName){
    // 5      Call person
    console.log(`calling ${personName}`);
    return;
} else if(personName < currentPage){
    right = middle - 1;
} else {
    left = middle + 1;
}
}
console.log (`${personName} not found in contacts`);
// 6  Else if person is earlier in book
// 7      Open to middle of left half of book
// 8      Go back to line 3
// 9  Else if person is later in book
// 10     Open to middle of right half of book
// 11     Go back to line 3
// 12 Else
// 13     Quit
}
const contacts = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"];
findPerson(contacts, "Eve"); 
findPerson(contacts, "Zara");