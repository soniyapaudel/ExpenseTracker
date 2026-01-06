document.addEventListener("DOMContentLoaded", function () {
    const showFormBtn = document.getElementById("showFormBtn");
    const expenseForm = document.getElementById("expenseForm");
    const expenseTable = document.querySelector(".table tbody");

    expenseForm.addEventListener("submit", function (e) {
        e.preventDefault();

        // Get form values from db---
        const type = document.getElementById("typeSelect").value;
        const amount = this.amount.value;
        const description = this.description.value;
        const category = this.category.value;
        const date = this.date.value;

        // create a new row 

        const row = document.createElement("tr");

        row.innerHTML = `
                <td>${type}</td>
                <td>${amount}</td>
                <td>${description}</td>
                <td>${category}</td>
                <td>${date}</td> `;

        // Append row to table
        expenseTable.appendChild(row);

        // Reset the form 
        expenseForm.reset();
        // Hide form after submission
        expenseForm.style.display = "none";

    });
    showFormBtn.addEventListener("click", () => {
        //toggle from visibility
        if (expenseForm.style.display === "none" || expenseForm.style.display === "") {
            expenseForm.style.display = "block";
        } else {
            expenseForm.style.display = "none";
        }
    });

    // Dynamic form category choices---

    const typeSelect = document.getElementById('typeSelect');
    const categorySelect = document.getElementById('category');

    // Expense and Income categories from Django context

    const expenseCategories = JSON.parse(document.getElementById('expense-data').textContent);

    const incomeCategories = JSON.parse(document.getElementById('income-data').textContent);

    typeSelect.addEventListener('change', function () {
        const categories = this.value === 'Expense' ? expenseCategories : incomeCategories;

        categorySelect.innerHTML = '<option value="">Select Category</option>';

        categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat[0]; // if your tuples are like ["Groceries", "Groceries"]
            option.textContent = cat[1];
            categorySelect.appendChild(option);
        });
    });

});

