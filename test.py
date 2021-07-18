import pylex_lite

string = """
if (n == 0) { n = 1; }

if (this and not that) {
    x = 1;
}

if (this or that) {
    x = 1;
}

if (this) {
    that = false;
} else {
    that = true;
}
"""

i = 0
buf = ""
tokens = []
while True:
    # Check for out of range
    if i > len(string) - 2:
        break

    # Get current and next characters
    cur = string[i]
    nxt = string[i + 1]

    # Continue to next if the characters is whitespace
    if pylex_lite.is_char_whitespace(cur):
        i += 1
        continue

    # Add the character to the buffer
    buf += cur

    # If the current characters ends the token,
    # append the buffer to the tokens list
    if pylex_lite.ends_token(cur, nxt):
        tokens.append(buf)
        buf = ""
    i += 1

print(tokens)
