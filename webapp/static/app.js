var ws = new WebSocket("ws://127.0.0.1:9000/")

ws.onmessage = function (event) {
    console.log("Message: ".concat(event))
    // Execute on message received
};

