const BASE_URL = 'https://4875c991-9a39-4661-90d6-921cf8eb0028.mock.pstmn.io'; // Base URL constant
let bondDataCache = []; // Variable to store bond data

// Function to fetch bond data from the API
async function fetchBondData() {
    try {
        const response = await fetch(`${BASE_URL}/getbonds`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }); // Updated endpoint

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        bondDataCache = data.bonds; // Store the bonds array in the cache
        return bondDataCache; // Return the bonds array
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        return []; // Return an empty array on error
    }
}

// Function to fetch order book data from the API
async function fetchOrderBookData() {
    try {
        const response = await fetch(`${BASE_URL}/getorderbook`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }); // Updated endpoint

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data.orderbook; // Return the orderbook array
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        return []; // Return an empty array on error
    }
}

// Function to fetch news data from the API
async function fetchNews() {
    try {
        const response = await fetch(`${BASE_URL}/getnews`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }); // Updated endpoint

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data.news; // Return the news string
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        return 'Failed to load news.'; // Return a fallback message on error
    }
}

async function fillTable() {
    const bondDataElement = document.getElementById('bond-data');
    const tableHeadersElement = document.getElementById('table-headers');
    const bonds = await fetchBondData(); // Fetch bond data

    // Set table headers dynamically based on the first bond object
    if (bonds.length > 0) {
        Object.keys(bonds[0]).forEach(key => {
            const th = document.createElement('th');
            th.textContent = key; // Set header text
            tableHeadersElement.appendChild(th); // Append to the header row
        });
    }

    // Populate the table body with bond data
    bonds.forEach(item => {
        const row = document.createElement('tr');
        row.className = "clickable-row";
        row.onclick = () => fillForm(item['Security Name'], item['LTP']);
        Object.values(item).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value; // Set cell text
            row.appendChild(td); // Append to the row
        });
        bondDataElement.appendChild(row); // Append the row to the table body
    });
}

async function fillOrderBook() {
    const orderBookDataElement = document.getElementById('order-book-data');
    const orderBookHeadersElement = document.getElementById('order-book-headers');
    const orderbook = await fetchOrderBookData(); // Fetch order book data

    // Set table headers dynamically based on the first order book object
    if (orderbook.length > 0) {
        Object.keys(orderbook[0]).forEach(key => {
            const th = document.createElement('th');
            th.textContent = key; // Set header text
            orderBookHeadersElement.appendChild(th); // Append to the header row
        });
    }

    // Populate the table body with order book data
    orderbook.forEach(item => {
        const row = document.createElement('tr');
        Object.values(item).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value; // Set cell text
            row.appendChild(td); // Append to the row
        });
        orderBookDataElement.appendChild(row); // Append the row to the table body
    });
}

async function fillNews() {
    const newsContentElement = document.getElementById('news-content');
    const news = await fetchNews(); // Fetch news data
    newsContentElement.textContent = news; // Set the news content
}

function fillForm(securityName, ltp) {
    document.getElementById("securityNameInput").value = securityName;
    document.getElementById("priceInput").value = ltp;
}

// Popup and Overlay Functions
async function fetchBonds() {
    try {
        const bonds = bondDataCache; // Use cached bond data
        const bondSelect = document.getElementById('bond');
        bondSelect.innerHTML = bonds.map(bond => `<option value="${bond['Security Name']}">${bond['Security Name']}</option>`).join('');
    } catch (error) {
        console.error('Error fetching bonds:', error);
    }
}

function openPopup() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
    fetchBonds();
}

function closePopup() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
}

function calculate() {
    let bond = document.getElementById('bond').value;
    let type = document.getElementById('type').value;
    let value = document.getElementById('inputValue').value;
    alert(`Calculating ${type} for bond ${bond} with value ${value}`);
}

// Function to fetch PnL data from the API
async function fetchPnLData() {
    try {
        const response = await fetch(`${BASE_URL}/getpnl`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }); // Updated endpoint

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data.pnl; // Return the PnL data
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        return { realised: 'Error', balance: 'Error' }; // Return error structure on error
    }
}

// Function to display PnL data
async function displayPnL() {
    const pnlData = await fetchPnLData();
    const pnlElement = document.getElementById('pnl-display');
    const realisedGainElement = document.getElementById('realised-gain');
    const balanceElement = document.getElementById('balance');

    realisedGainElement.textContent = `Realised P/L: ${pnlData.realised}`;
    balanceElement.textContent = `Balance: ${pnlData.balance}`;

    realisedGainElement.style.color = pnlData.realised >= 0 ? 'green' : 'red';
    balanceElement.style.color = pnlData.balance >= 0 ? 'green' : 'red';
}

// Function to fetch chart data from the API
async function fetchChartData() {
    try {
        const response = await fetch(`${BASE_URL}/getchart`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }); // Updated endpoint

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data.chart; // Return the chart data
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        console.error('Error fetching chart data:', error);
        return { title: 'Error', xAxis: '', yAxis: '', data: [] }; // Return error structure on error
    }
}

// Function to render the chart
async function renderChart() {
    const chartData = await fetchChartData();
    const ctx = document.getElementById('yieldChart')?.getContext('2d');
    const labels = chartData.data.map(point => point.date);
    const yields = chartData.data.map(point => point.yield);

    const yieldChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: chartData.title,
                data: yields,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: chartData.xAxis
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: chartData.yAxis
                    }
                }
            }
        }
    });
}

// Call fillTable, fillOrderBook, fillNews, renderChart, and displayPnL on page load
window.onload = async () => {
   fillTable();
   //fillOrderBook();
   //fillNews(); // Fetch and display news
   //displayPnL(); // Fetch and display PnL data
   //renderChart();
};
