// TODO: add loading spinner
// NOTE: might need to handle larger datasets differently
async function loadDashboardData() {
    try {
        const timestamp = new Date().getTime();
        const response = await fetch("data/processed/dashboard.json?t=" + timestamp);
        
        if (!response.ok) {
            throw new Error("HTTP error! status: " + response.status);
        }
        
        const data = await response.json();
        console.log("Loaded data:", data);
        
        updateStats(data);
        renderTransactions(data.recent_transactions || []);
        updateTimestamp();
        
    } catch (error) {
        console.error("Failed to load dashboard data:", error);
        alert("Error loading data: " + error.message);
    }
}

function formatRWF(amount) {
    const formatted = new Intl.NumberFormat("en-US").format(amount);
    return "RWF " + formatted;
}

function updateStats(data) {
    document.getElementById("total-transactions").textContent = data.total_transactions || 0;
    document.getElementById("total-amount").textContent = formatRWF(data.total_amount || 0);
    document.getElementById("category-count").textContent = data.categories ? data.categories.length : 0;
}

function updateTimestamp() {
    const now = new Date();
    const timeString = now.toLocaleTimeString("en-US", { 
        hour: "2-digit", 
        minute: "2-digit" 
    });
    document.getElementById("last-update").textContent = timeString;
}

function renderTransactions(transactions) {
    const tbody = document.getElementById("transactions-body");
    tbody.innerHTML = "";
    
    if (transactions.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 2rem; color: #999;">No transactions available</td></tr>';
        return;
    }
    
    transactions.forEach(function(tx) {
        const row = document.createElement("tr");
        row.innerHTML = 
            "<td><strong>" + tx.date + "</strong></td>" +
            "<td>" + tx.type + "</td>" +
            '<td style="color: #10b981; font-weight: 600;">' + formatRWF(tx.amount) + "</td>" +
            '<td><span style="background: #667eea; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.85rem;">' + tx.category + "</span></td>" +
            '<td style="font-family: monospace;">' + tx.phone + "</td>";
        tbody.appendChild(row);
    });
}

console.log("Script loaded");
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM ready, loading data...");
    loadDashboardData();
});



