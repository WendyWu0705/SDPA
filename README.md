# Flower Shop Simulator

A text-based flower shop simulation game built with Python, implementing object-oriented programming principles to simulate monthly business operations of a flower shop.

## Project Overview

This project is a comprehensive flower shop management simulator that allows players to manage a flower shop over multiple months. Players must make strategic decisions about staff management, bouquet production, inventory management, and vendor selection to maximize profits while avoiding bankruptcy.

## Features

### Core Functionality

- **Monthly Business Simulation**: Run the shop for multiple months, making decisions each month
- **Staff Management**: Hire and fire florists (1-4 employees allowed)
- **Bouquet Production**: Three types of bouquets with different requirements:
  - Fern-tastic
  - Be-Leaf in Yourself
  - You Rose to the Occasion
- **Inventory Management**: Manage greenhouse capacity with depreciation
- **Vendor Selection**: Choose between two vendors for each flower type
- **Financial Tracking**: Monitor cash flow, expenses, and profits

### Advanced Features

#### 1. Employee Specialization
- Employees can specialize in a specific bouquet type
- Specialized employees take **half the time** to make their specialized bouquets
- Improves production efficiency and allows for strategic workforce planning

#### 2. Salary Incentive System
- **Normal Employees**: £15.5/hour
- **Senior Managers**: £20/hour
- Senior managers provide a **50% price increase** on all bouquets
- Strategic decision: higher salary cost vs. increased revenue


## Project Structure

```
.
├── main.py              # Main entry point
├── shop.py              # Shop class - manages employees and operations
├── florist.py           # Florist class - employee management
├── check_status.py      # Target class - order validation and checks
├── flower_shop.py       # Bouquet, vendor classes - core business logic
├── solo.py              # one_run() function - monthly simulation
├── part2.ipynb          # Part 2: Data Analytics (Jupyter notebook)
└── README.md            # This file
```
## How to Run

### Prerequisites
- Python 3.x
- NumPy library

### Installation
```bash
pip install numpy
```

### Running the Simulation
```bash
python main.py
```

### Game Flow
1. **Initial Setup**: Start with £7,500 balance
2. **Monthly Cycle**:
   - Manage staff (add/remove, set specialization and salary level)
   - Set bouquet production targets
   - System validates:
     - Market demand limits
     - Greenhouse capacity
     - Labor capacity (considering specialization)
   - Choose vendors for restocking
   - View monthly summary:
     - Income and expenses
     - Cash flow
     - Remaining inventory
     - Staff status
3. **Continue**: Repeat for desired number of months
4. **Game Over**: If balance reaches £0 or below


## Class Design

### `shop` (shop.py)
Main shop management class that handles:
- Employee management (hiring/firing)
- Salary calculation (normal vs. senior)
- Revenue calculation with senior manager bonus
- Employee count validation (1-4 employees)

**Key Methods:**
- `input_florist()`: Interactive employee management
- `process_input_florist()`: Process and validate employee changes
- `operation(target)`: Calculate monthly revenue

### `florist` (florist.py)
Employee information management:
- Stores employee data: name, specialization, salary level
- Handles adding/removing employees
- Validates employee information

**Key Methods:**
- `add_florist(n)`: Add new employees with specialization and salary level
- `rem_florist(n)`: Remove existing employees
- `has_senior_manager()`: Check for senior manager presence

### `Target` (check_status.py)
Order validation and production time calculation:
- Validates order quantities against market demand
- Checks greenhouse capacity
- Calculates production time considering specialization
- Validates labor capacity

**Key Methods:**
- `calculate_making_time(target)`: Calculate time with specialization
- `input_quantity()`: Get order quantities from user
- `check_capacity()`: Validate greenhouse capacity
- `labour_check()`: Validate sufficient labor

### `bouquet` (flower_shop.py)
Bouquet production and inventory management:
- Manages bouquet composition and requirements
- Calculates material consumption
- Handles greenhouse depreciation
- Calculates replenishment costs

**Key Methods:**
- `operation()`: Calculate material requirements and costs
- `repleinishment(vendor_price)`: Calculate restocking costs

### `vendor` (flower_shop.py)
Vendor management:
- Two vendors: Evergreen Essentials and FloraGrow Distributors
- Different prices for each flower type
- Interactive vendor selection

## Bouquet Specifications

| Bouquet | Greenery | Roses | Daisies | Time (minutes) | Price (£) |
|---------|----------|-------|---------|----------------|-----------|
| Fern-tastic | 4 | 0 | 2 | 20 | 18.5 |
| Be-Leaf in Yourself | 2 | 1 | 3 | 30 | 17.5 |
| You Rose to the Occasion | 2 | 4 | 2 | 45 | 32.5 |

### Market Demand (per month)
- Fern-tastic: 175
- Be-Leaf in Yourself: 100
- You Rose to the Occasion: 250

## Greenhouse Management

### Capacity Limits
- Roses: 200 bunches
- Daisies: 250 bunches
- Greenery: 400 bunches

### Depreciation Rates (monthly)
- Roses: 40%
- Daisies: 15%
- Greenery: 50%

### Operating Costs (per unit)
- Roses: £1.5
- Daisies: £0.8
- Greenery: £0.2

## Vendor Prices

### Evergreen Essentials
- Roses: £2.8/bunch
- Daisies: £1.5/bunch
- Greenery: £0.95/bunch

### FloraGrow Distributors
- Roses: £1.6/bunch
- Daisies: £1.2/bunch
- Greenery: £1.8/bunch


## Example Gameplay

```
Welcome to the FlowerShop Simulator!
---------------------------------------------------------------
How many months would you like to run the game for? 3

Month 1 

Before the month starts, there are some owner actions for you to carry out.
First, review the number of staff, then decide how many bouquets to sell.
Current number of florists: 0
How many florists do you want to add this month? 1
Please input florist name (one at a time): Alice

Set specialization for Alice (specialization allows employees to make specific bouquets in half the time):
0 = Fern-tastic
1 = Be-Leaf in Yourself
2 = You Rose to the Occasion
Press Enter to skip = No specialization
Please enter specialization type (0/1/2/Enter): 0

Set salary level for Alice:
n = Normal employee (£15.5/hour)
s = Senior manager (£20/hour, increases all bouquet prices by 50%)
Please enter salary level (n/s, default n): n
...
```

## Key Design Decisions

### Object-Oriented Design
- **Separation of Concerns**: Each class handles a specific aspect of the business
- **Encapsulation**: Employee data encapsulated in `florist` class
- **Modularity**: Easy to extend or modify individual components

### Specialization System
- **Efficiency Gain**: Specialized employees are 2x faster for their specialty
- **Strategic Planning**: Players must balance specialization vs. flexibility
- **Time Calculation**: Parallel production assumed (max time across bouquet types)

### Salary Incentive System
- **Risk-Reward**: Higher cost (£20 vs £15.5/hour) for 50% price increase
- **Break-even Analysis**: Players must calculate if senior manager is profitable
- **Flexible Strategy**: Can hire/fire senior managers monthly

## Error Handling

The system includes comprehensive error handling:
- **Input Validation**: All user inputs validated
- **Capacity Checks**: Prevents impossible orders
- **Labor Validation**: Ensures sufficient workforce
- **Market Demand**: Prevents over-ordering
- **Employee Limits**: Enforces 1-4 employee constraint
- **Duplicate Names**: Prevents duplicate employee names

## Part 2: Data Analytics

The project also includes a data analytics component (`part2.ipynb`) that:
- Crawls real-world datasets
- Performs data cleaning and preparation
- Conducts exploratory data analysis
- Answers complex questions about the data
- Provides insights and conclusions

## Future Enhancements

Potential improvements:
- Save/load game state
- Difficulty levels
- More bouquet types
- Seasonal demand variations
- Customer satisfaction metrics
- Marketing campaigns
- Equipment upgrades

## Author

Wendy Wu 
Email: eu24054@bristol.ac.uk
Student number:  
University of Bristol - SDPA Coursework

## License

This project is part of academic coursework.


