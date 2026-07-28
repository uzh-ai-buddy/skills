# Course-Data Topic Vocabulary

`search_courses_by_criteria` and `search_courses_combined` use **different, non-interchangeable**
topic vocabularies for their `topic_names` parameter. Never pass a name from one tool's list to
the other tool — read the section below for the tool you are calling and use exact names from it.

## `search_courses_by_criteria` — granular topics

Valid topic names (use exact names):

- 'Banking'
- 'Financial Markets'
- 'Risk Management'
- 'Valuation'
- 'Business Administration'
- 'Human Resource Management'
- 'Strategic Management'
- 'Economic Policy'
- 'Data Science'
- 'Empirical Research'
- 'Software Development'
- 'Machine Learning'
- 'Hedging Strategies'
- 'Investment Analysis'
- 'Financial Accounting'
- 'Corporate Governance'
- 'Decision-Making Tools'
- 'Data Visualization'
- 'Corporate Social Responsibility'
- 'Sustainability'
- 'Innovation'
- 'Economic Theory'
- 'Artificial Intelligence'
- 'Digital Marketing'
- 'Entrepreneurship'
- 'Behavioral Economics'
- 'Operations Management'
- 'Economic Principles'
- 'Monetary Policy'
- 'Globalization'
- 'Business Ethics'
- 'Microeconomics'
- 'Organizational Behavior'
- 'Corporate Finance'
- 'Capital Structure'
- 'Political Economy'
- 'Market Research'
- 'Portfolio Management'
- 'Project Management'

Topic abbreviation mappings:

- "ai": "Artificial Intelligence",
- "cf": "Corporate Finance",
- "accounting": "Financial Accounting",
- "ml": "Machine Learning",
- "programming": "Software Development",

## `search_courses_combined` — clustered topics

Valid topic names (use exact names):

- "Accounting & Financial Reporting"
- "Artificial Intelligence & Machine Learning"
- "Banking & Financial Institutions"
- "Business Strategy & Management"
- "Computer Science Fundamentals & Theory"
- "Computer Systems & Networking"
- "Corporate Finance & Valuation"
- "Data Science & Analytics"
- "Economics & Economic Policy"
- "Financial Markets & Instruments"
- "Governance, Ethics & Sustainability"
- "Human–Computer Interaction & Collaboration"
- "Innovation, Entrepreneurship & Leadership"
- "Investment & Portfolio Management"
- "Marketing & Customer Analytics"
- "Mathematics & Optimization"
- "Operations & Supply Chain Management"
- "Quantitative Methods & Econometrics"
- "Risk Management & Insurance"
- "Software Engineering & Development"

Topic abbreviations supported:

- "AI", "ML" → "Artificial Intelligence & Machine Learning"
- "HCI" → "Human–Computer Interaction & Collaboration"
- "data science" → "Data Science & Analytics"
