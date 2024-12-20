-- 用户表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    position VARCHAR(50),
    department VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 文档表
CREATE TABLE documents (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    document_no VARCHAR(50) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    version VARCHAR(20),
    status VARCHAR(20) NOT NULL,
    file_path VARCHAR(255),
    description TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 物料表
CREATE TABLE materials (
    id INT PRIMARY KEY AUTO_INCREMENT,
    material_no VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    specification TEXT,
    unit VARCHAR(20),
    price DECIMAL(10,2),
    stock_quantity INT DEFAULT 0,
    status VARCHAR(20) NOT NULL,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 变更表
CREATE TABLE changes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    change_no VARCHAR(50) NOT NULL UNIQUE,
    title VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    description TEXT,
    impact_analysis TEXT,
    approval_status VARCHAR(20),
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 项目表
CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    project_no VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    start_date DATE,
    end_date DATE,
    manager_id INT,
    description TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES users(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 供应商表
CREATE TABLE suppliers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_no VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(50),
    contact_phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    status VARCHAR(20) NOT NULL,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- 项目-文档关联表
CREATE TABLE project_documents (
    project_id INT,
    document_id INT,
    PRIMARY KEY (project_id, document_id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

-- 项目-物料关联表
CREATE TABLE project_materials (
    project_id INT,
    material_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);

-- 供应商-物料关联表
CREATE TABLE supplier_materials (
    supplier_id INT,
    material_id INT,
    unit_price DECIMAL(10,2),
    PRIMARY KEY (supplier_id, material_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
); 