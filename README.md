# CSRtoOWL

Pipeline from CSR (Counselling Service Request Form) to OWL Practice to efficiently and securely transport client data from a form to the main database that is used.

## Setup & Installation

### Prerequisites

* Python 3.10+
* Git

### 1. Clone the Repository

```
git clone git@github.com:YOUR-USERNAME/CSRtoOWL.git
```

### 2. Set Up Virtual Environment

```
python -m venv .venv

# On Mac/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
playwright install
```

### 4. Configure Environment Variables

Copy the example environment file to create your own local configuration:

```
cp .env.example .env
```

Open the created `.env` file and replace the placeholder URL with the clinic's login URL.

## Contributions

Contributions are highly encouraged! Whether it is adding support for a new form layout, fixing a bug, or improving the browser automation, all is accepted and appreciated.

### Development Guidelines

* **Protect Patient Data:** Absolutely NO real patient data or real clinic URLs should ever be committed to this repository. Please just use dummy data.

* **Keep it Modular:** If you are modifying a certain piece of logic then keep the changes in the right place.

* **Branch Naming:** Create cleanly named branches for feature or bug fixes.

### Submitting a Pull Request

1. A typical clear and descriptive commit message is required.

2. Push your branch to your forked repository.

3. Open a Pull Request against the `ain branch of the original repo.

4. In your PR description, explain what you changed and why.
