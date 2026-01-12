// Load dashboard data from JSON file
async function loadDashboardData() {
    try {
        const response = await fetch('data/processed/dashboard.json');
        const data = await response.json();
        
        updateSummaryCards(data);
        displayTransactions(data.recent_transactions || []);
        
    } catch (error) {
        console.error('Could not load data:', error);
        showError();
    }
}

function updateSummaryCards(data) {
    document.getElementById('total-transactions').textContent = data.total_transactions || 0;
    document.getElementById('total-amount').textContent = `$${(data.total_amount || 0).toFixed(2)}`;
    document.getElementById('category-count').textContent = data.categories?.length || 0;
}

function displayTransactions(transactions) {
    const tbody = document.querySelector('#transactions tbody');
    tbody.innerHTML = '';
    
    transactions.forEach(tx => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${tx.date}</td>
            <td>${tx.type}</td>
            <td>$${tx.amount.toFixed(2)}</td>
            <td>${tx.category}</td>
            <td>${tx.phone}</td>
        `;
    });
}

function showError() {
    document.getElementById('total-transactions').textContent = 'Error loading data';
}

document.addEventListener('DOMContentLoaded', loadDashboardData);
