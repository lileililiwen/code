function generatePassword(length, includeSymbols = false) {
    // Define character set
    let characters = includeSymbols
      ? 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]\\:;?><,./-='
      : 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    // Generate password
    let password = '';
    for (let i = 0; i < length; i++) {
      password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return password;
  }

// Generate a 12-character password without symbols
let password1 = generatePassword(12);
console.log(password1);

// Generate a 16-character password with symbols
let password2 = generatePassword(16, true);
console.log(password2);
