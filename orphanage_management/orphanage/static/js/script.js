document.getElementById("id_donation_type").addEventListener("change", function () {
    const type = this.value;
    const amountField = document.getElementById("id_amount").parentElement;
    amountField.style.display = type === "money" ? "block" : "none";
});
