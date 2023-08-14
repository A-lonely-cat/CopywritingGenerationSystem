function generateText() {
    const input = document.getElementById("input").value;
    fetch("/generate_text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({input: input})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").value = data.generated_text;
    });
}