# <a id="Top-of-Page"> Welcome to the Web3 Ether Talent Pool!</a>
#### A web app for hiring and transacting on the Ethereum blockchain.

***
## <a id="Contents">Cotents</a>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
[Bottom of Page](#Bottom-of-Page)<br>

***
## <a id="Project-Description">Project Description</a>
This project, provides an interface for sourcing Web3 development talent. The Web3 Ether Talent Pool project provides the Fintech Finder page. This page allows clients to identify talent, specify the work demand, and transact compensation via the cryptocurrency Ether.

#### A summary of what's under the hood:    
This project utilizes the Python library <a href="https://web3py.readthedocs.io/en/stable/" target="_blank">Web3.py</a>, for interacting with Ethereum. This library is used to provide blockchain references and lookups, execute transactions, and update costs and balances.

The Fintech Finder page is generated with the <a href="https://streamlit.io/" target="_blank">streamlit</a> web app framework to provide an accurate and responsive utility for selecting talent.

#### Project layout:
The layout of essentials for this project is show below.
.<br>
├── .env<br>
├── crypto_wallet.py<br>
├── fintech_finder.py<br>
├── img<br>
│   ├── 19-0-infura-sign-up.png<br>
│   ├── ash.jpeg<br>
│   ├── client-etherscan-kovan.png<br>
│   ├── jo.jpeg<br>
│   ├── kendall.jpeg<br>
│   ├── lane-etherscan-kovan.png<br>
│   ├── lane.jpeg<br>
│   ├── transaction-etherscan-kovan.png<br>
│   └── web-app.png<br>
├── LICENSE<br>
├── README.md<br>
├── requirements.txt<br>
├── SAMPLE.env<br>
├── setup.py<br>
├── static<br>
│   ├── fintech-01.jpg<br>
│   └── style.py<br>
├── streamlit_custom_components<br>
│   ├── copycontent_button<br>
│   │   ├── frontend<br>
│   │   │   └── build<br>
│   │   │       ├── asset-manifest.json<br>
│   │   │       ├── bootstrap.min.css<br>
│   │   │       ├── index.html<br>
│   │   │       ├── precache-manifest.7d28d4f1dd06fe1528c46b815edd1fb6.js<br>
│   │   │       ├── service-worker.js<br>
│   │   │       └── static<br>
│   │   │           └── js<br>
│   │   │               ├── 2.bd9b94bf.chunk.js<br>
│   │   │               ├── 2.bd9b94bf.chunk.js.LICENSE.txt<br>
│   │   │               ├── 2.bd9b94bf.chunk.js.map<br>
│   │   │               ├── main.5ac0fb29.chunk.js<br>
│   │   │               ├── main.5ac0fb29.chunk.js.map<br>
│   │   │               ├── runtime-main.547c5a5e.js<br>
│   │   │               └── runtime-main.547c5a5e.js.map<br>
│   │   ├── test.py<br>
│   │   └── __init__.py<br>
│   └── crypto_account_stack<br>
│       ├── frontend<br>
│       │   └── build<br>
│       │       ├── asset-manifest.json<br>
│       │       ├── bootstrap.min.css<br>
│       │       ├── index.html<br>
│       │       ├── precache-manifest.e4affc5c9aa6a411f03be436b6d71409.js<br>
│       │       ├── service-worker.js<br>
│       │       └── static<br>
│       │           └── js<br>
│       │               ├── 2.bd102428.chunk.js<br>
│       │               ├── 2.bd102428.chunk.js.LICENSE.txt<br>
│       │               ├── 2.bd102428.chunk.js.map<br>
│       │               ├── main.453cc1a2.chunk.js<br>
│       │               ├── main.453cc1a2.chunk.js.map<br>
│       │               ├── runtime-main.eab36c2e.js<br>
│       │               └── runtime-main.eab36c2e.js.map<br>
│       ├── test.py<br>
│       └── __init__.py<br>
└── tree.txt<br>

**Note:** <code>.env</code> is only a refernece to show how and where it should be in the project structure. Please use <code>SAMPLE.env</code> as a reference template for your own <code>.env</code> file.

***
## <a id="Technologies">Technologies</a>
<a href="https://docs.python.org/release/3.8.0/" title="https://docs.python.org/release/3.8.0/"><img src="https://img.shields.io/badge/python-3.7.4%2B-red">
<a href="https://github.com/theskumar/python-dotenv" title="https://github.com/theskumar/python-dotenv"><img src="https://img.shields.io/badge/streamlit-1.1.0-green"></a>
<a href="https://github.com/ethereum/eth-tester" title="https://github.com/ethereum/eth-tester"><img src="https://img.shields.io/badge/eth--tester-0.5.0b3-red"></a>
<a href="https://github.com/trezor/python-mnemonic" title="https://github.com/trezor/python-mnemonic"><img src="https://img.shields.io/badge/mnemonic-0.19-green"></a>
<a href="https://github.com/kigawas/python-bip44" title="https://github.com/kigawas/python-bip44"><img src="https://img.shields.io/badge/bip44-0.1.0-blue"></a>
<br>
<a href="requirements.txt" title="requirements.txt">Requirements List</a><br><br>
In addition to the Python installation requirements, you will also need to open an account with Infura API. To create an Infura account, navigate to the Infura website's <a href="https://infura.io/register" target="_blank">registration page</a>, then register for an account, as shown in the following image:<br>
<img src="img/19-0-infura-sign-up.png" alt="Infura registration page">

***
## <a id="Installation-Guide">Installation Guide</a>
### Project Installation
To install <a href="https://github.com/jasonjgarcia24/web3-ether-talent-pool" title="https://github.com/jasonjgarcia24/web3-ether-talent-pool">web3-ether-talent-pool</a>, type <code>git clone https://github.com/jasonjgarcia24/web3-ether-talent-pool.git</code> into bash in your prefered local directory.<br><br>
Alternatively, you can navigate to the same address (<code>https://github.com/jasonjgarcia24/web3-ether-talent-pool.git</code>) and download the full <code>main</code> branch's contents as a zip file to your prefered local directory.<br>

### Setting Environment Variables
A <code>.env</code> file is required for use with the <a href="https://alpaca.markets/" target="_blank">Infura API</a>. The Infura API will facilitate blockchain transactions over the Ethereum network.

| Environment                               | Description                |
| ----------------------------------------- | -------------------------- |
| MNEMONIC=&lt;mnemonic&gt;                 | Your Client's ETH Mnemonic |
| WEB3_INFURA_PROJECT_ID=&lt;secret_key&gt; | Your Infura Project ID     |

***
## <a id="Usage">Usage</a>
This web app interface is shown below:<br>
<img src="img/web-app.png" alt="fintech finder web app"><br>

When navigating to the client's account on <a href="https://kovan.etherscan.io/" target="_blank">Kovan Etherscan</a>, we can see related transactions:<br>
<img src="img/client-etherscan-kovan.png" alt="client kovan etherscan"><br>
    
Additionally, on the Kovan Etherscan page, we can see the corresponding transactions:<br>
<img src="img/transaction-etherscan-kovan.png" alt="transaction kovan etherscan"><br>
    
And finally, we can also view the account of the recipient (our Fintech professional):<br>
<img src="img/lane-etherscan-kovan.png">
***
## <a id="Contributors">Contributors</a>
Currently just me :)<br>

***
## <a id="License">License</a>
Each file included in this repository is licensed under the <a href="https://github.com/jasonjgarcia24/web3-ether-talent-pool/blob/e0f0508e2d1a41c32d608373a7d796601ee42daa/LICENSE" title="github.com/jasonjgarcia24/financial-planning-tools/blob/main/LICENSE">MIT License.</a>

***
[Top of Page](#Top-of-Page)<br>
[Contents](#Contents)<br>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
<a id="Bottom-of-Page"></a>
