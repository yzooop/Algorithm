function solution(wallpaper) {
    let map = new Map()
    let rows = []
    let cols = []
    
    wallpaper.forEach((items, row) => {
        if (items.includes("#")) {
            rows.push(row)
        }
        [...items].forEach((item, col) => {
            if (item === "#") {
                cols.push(col)
            }
        })
    })
    map.set("row_max", Math.max(...rows) + 1)
    map.set("row_min", Math.min(...rows))
    map.set("col_max", Math.max(...cols) + 1)
    map.set("col_min", Math.min(...cols))
    
    return [map.get("row_min"), map.get("col_min"), map.get("row_max"), map.get("col_max")]
}