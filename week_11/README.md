# Week 11: The Internet and Web

**Big Idea:** CSN (Computing Systems and Networks)

---

## Learning Objectives

By the end of this week, you should be able to:
- Explain how the Internet works (packets, protocols, routing)
- Understand the World Wide Web (HTTP, URLs, HTML)
- Create basic web pages with HTML and CSS
- Understand client-server architecture

---

## AP CSP Concepts

### CSN-1: The Internet
The **Internet** is a network of networks - billions of devices connected globally.

### How Data Travels
1. **Packets**: Data is broken into small packets
2. **Routing**: Packets travel through multiple routers
3. **Reassembly**: Packets are reassembled at destination

### Key Protocols
| Protocol | Purpose | Example |
|----------|---------|---------|
| **IP** | Addressing devices | 192.168.1.1 |
| **TCP** | Reliable data transfer | Ensures packets arrive |
| **HTTP/HTTPS** | Web communication | Requesting web pages |
| **DNS** | Domain name lookup | google.com → IP address |

### IP Addresses
- **IPv4**: 32 bits (e.g., 192.168.1.1)
- **IPv6**: 128 bits (e.g., 2001:0db8:85a3::8a2e:0370:7334)
- IPv6 created because IPv4 addresses ran out!

### The World Wide Web
The **Web** is a service that runs ON the Internet (not the same thing!)

**URL Structure:**
```
https://www.example.com:443/path/page.html?query=value
  │         │          │        │             │
  │         │          │        │             └─ Query string
  │         │          │        └─ Path
  │         │          └─ Port
  │         └─ Domain name
  └─ Protocol (secure)
```

### Client-Server Model
```
[Client]  ──HTTP Request──>  [Server]
(Browser)                    (Web Server)
          <─HTTP Response──
            (HTML, CSS, JS)
```

### HTML Basics
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">A link</a>
    <img src="image.jpg" alt="Description">
</body>
</html>
```

### CSS Basics
```css
/* Select by element */
h1 {
    color: blue;
    font-size: 24px;
}

/* Select by class */
.highlight {
    background-color: yellow;
}

/* Select by ID */
#header {
    padding: 20px;
}
```

### Fault Tolerance
The Internet is designed to be **fault tolerant**:
- Multiple paths between devices
- If one router fails, packets take another route
- Redundancy ensures reliability

---

## Practice Files

1. **index.html** - Basic HTML structure
2. **styles.css** - CSS styling
3. **01_dom_basics.html** - JavaScript DOM interaction
4. **02_events_practice.html** - Event handling

---

## AP-Style Practice Questions

### Question 1
Which protocol is used to securely transfer web pages?
- A) HTTP
- B) HTTPS
- C) TCP
- D) DNS

<details>
<summary>Answer</summary>
B) HTTPS — The 'S' stands for Secure (encrypted)
</details>

### Question 2
What happens when you type "google.com" in your browser?
- A) Your computer directly contacts Google's server
- B) DNS converts the domain to an IP address, then your computer contacts the server
- C) The browser stores the webpage locally
- D) Google sends the page without any request

<details>
<summary>Answer</summary>
B) DNS converts the domain to an IP address, then your computer contacts the server
</details>

### Question 3
Why was IPv6 created?
- A) IPv4 was too fast
- B) IPv4 addresses were running out
- C) IPv4 was too secure
- D) IPv6 uses smaller addresses

<details>
<summary>Answer</summary>
B) IPv4 addresses were running out — IPv4 has ~4.3 billion addresses; IPv6 has 340 undecillion
</details>

### Question 4
What makes the Internet fault tolerant?
- A) All data is encrypted
- B) Data travels through a single central server
- C) Multiple paths exist between devices
- D) Packets are never lost

<details>
<summary>Answer</summary>
C) Multiple paths exist between devices — If one path fails, data can take another route
</details>

### Question 5
In the URL `https://shop.example.com/products?id=123`, what is "shop.example.com"?
- A) Protocol
- B) Domain name (host)
- C) Path
- D) Query string

<details>
<summary>Answer</summary>
B) Domain name (host)
</details>

---

## Key Takeaways

1. The Internet is a network of networks using standardized protocols
2. Data travels as packets through multiple routers
3. DNS translates domain names to IP addresses
4. HTTP/HTTPS enables web communication
5. The web uses client-server architecture
6. Redundancy makes the Internet fault tolerant
