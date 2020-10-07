DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS budgets;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255)
);

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    total_budget DECIMAL(12,2)
);


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(12,2),
    company_id SERIAL REFERENCES companies(id),
    tag_id SERIAL REFERENCES tags(id)
);
