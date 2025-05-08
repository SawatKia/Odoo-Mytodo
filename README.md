# Odoo Mytodo Project Setup
## Prerequisites
- Python 3.11
- PostgreSql 14+
- Git

## steps
1. clone Odoo 18 Community Edition
```bash
# Create project directory
mkdir D:\parent1\parent2\odoo18
cd D:\parent1\parent2\odoo18

# Clone Odoo 18 Community
git clone -b 18.0 --single-branch --depth 1 https://github.com/odoo/odoo.git community
```
Note: see `project_strucutre.txt` for more detail
2. Create Python virtual enironment
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install Odoo dependencies
cd community
pip install -r requirements.txt
```
3. config vsCode with provide Configuration
4. apply odoo.conf to `launvh.json` if not provided
5. create odoo database user
```
CREATE USER odoo WITH PASSWORD 'odoo';
ALTER USER odoo WITH SUPERUSER;
```
6. Access wen interface at `http://localhost:8069

any error visit: [running Odoo from sourcce](https://www.odoo.com/documentation/18.0/administration/on_premise/source.html)
