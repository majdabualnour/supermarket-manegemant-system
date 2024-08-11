document.getElementById("barcodeInput").addEventListener("input", function() {
    var barcode = this.value;
    getProductInfo(barcode);
});

function getProductInfo(barcode) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_product_info?barcode=" + barcode, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var productInfo = JSON.parse(xhr.responseText);
            displayProductInfo(productInfo);
        }
    };
    xhr.send();
}

function displayProduct(product) {
    var productListDiv = document.getElementById("productList");
    var productDiv = document.createElement("div");
    productDiv.innerHTML = `
        <p>Name: ${product.name}</p>
        <p>Price: ${product.price}</p>
        <p>Category: ${product.category}</p>
        <input type="number" value="1" min="1" id="quantity${scannedProducts.length}" onchange="updateQuantity(${scannedProducts.length})">
    `;
    productListDiv.appendChild(productDiv);
}

function updateQuantity(index) {
    var quantity = document.getElementById("quantity" + index).value;
    scannedProducts[index - 1].quantity = parseInt(quantity);
}

function submitBill() {
    // Send scannedProducts array to server to submit the bill
    // Example code to send the array to the server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit_bill", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Handle response from server if needed
            alert("Bill submitted successfully!");
            // Clear scannedProducts array and product list on the page
            scannedProducts = [];
            document.getElementById("productList").innerHTML = '';
        }
    };
    xhr.send(JSON.stringify({ products: scannedProducts }));
}
   