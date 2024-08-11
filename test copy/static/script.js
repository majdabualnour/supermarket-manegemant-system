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

function displayProductInfo(productInfo) {
    var productInfoDiv = document.getElementById("productInfo");
    productInfoDiv.innerHTML = `
        <p>Name: ${productInfo.name}</p>
        <p>Price: ${productInfo.price}</p>
        <p>Category: ${productInfo.category}</p>
        <p>Quantity: ${productInfo.quantity}</p>
        <!-- Add more details as needed -->
    `;
}

