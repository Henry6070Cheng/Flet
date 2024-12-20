from .db import db

class MaterialDAL:
    @staticmethod
    def create_material(data):
        sql = """
            INSERT INTO materials 
            (material_no, name, category, specification, unit, price, 
            stock_quantity, status, created_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['material_no'],
            data['name'],
            data['category'],
            data.get('specification'),
            data.get('unit'),
            data.get('price'),
            data.get('stock_quantity', 0),
            data['status'],
            data['created_by']
        )
        return db.execute(sql, params)

    @staticmethod
    def get_material_by_id(material_id):
        sql = "SELECT * FROM materials WHERE id = %s"
        return db.fetch_one(sql, (material_id,))

    @staticmethod
    def get_material_by_no(material_no):
        sql = "SELECT * FROM materials WHERE material_no = %s"
        return db.fetch_one(sql, (material_no,))

    @staticmethod
    def get_all_materials(filters=None, page=1, page_size=10):
        where_clause = "WHERE 1=1"
        params = []

        if filters:
            if 'category' in filters:
                where_clause += " AND category = %s"
                params.append(filters['category'])
            if 'status' in filters:
                where_clause += " AND status = %s"
                params.append(filters['status'])
            if 'search' in filters:
                where_clause += " AND (name LIKE %s OR material_no LIKE %s)"
                search_term = f"%{filters['search']}%"
                params.extend([search_term, search_term])

        # 计算总数
        count_sql = f"SELECT COUNT(*) as total FROM materials {where_clause}"
        total = db.fetch_one(count_sql, tuple(params))['total']

        # 获取分页数据
        offset = (page - 1) * page_size
        sql = f"""
            SELECT m.*, u.username as creator_name
            FROM materials m
            LEFT JOIN users u ON m.created_by = u.id
            {where_clause}
            ORDER BY m.created_at DESC
            LIMIT %s OFFSET %s
        """
        params.extend([page_size, offset])
        materials = db.fetch_all(sql, tuple(params))

        return {
            'total': total,
            'items': materials,
            'page': page,
            'page_size': page_size,
            'total_pages': (total + page_size - 1) // page_size
        }

    @staticmethod
    def update_material(material_id, data):
        fields = []
        values = []
        for key, value in data.items():
            if key not in ['id', 'created_by', 'created_at', 'updated_at']:
                fields.append(f"{key} = %s")
                values.append(value)
        
        values.append(material_id)
        sql = f"UPDATE materials SET {', '.join(fields)} WHERE id = %s"
        return db.execute(sql, tuple(values))

    @staticmethod
    def delete_material(material_id):
        sql = "DELETE FROM materials WHERE id = %s"
        return db.execute(sql, (material_id,))

    @staticmethod
    def update_stock(material_id, quantity_change):
        sql = """
            UPDATE materials 
            SET stock_quantity = stock_quantity + %s 
            WHERE id = %s
        """
        return db.execute(sql, (quantity_change, material_id)) 