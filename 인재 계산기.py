def calculate_material_cost(area_py, material_type):
    material_costs = {'벽지' : 100000, '바닥재': 70000, '페인트': 30000}

    if material_type not in material_costs:
        raise ValueError("올바른 재료 타입(벽지, 바닥재, 페인트)을 입력 하십시오")

    cost_per_py = material_costs[material_type]

    total_cost = area_py * cost_per_py

    return total_cost

def main():
    try:
        area_py = float(input("방의 평수를 입력하시오: "))
        material_type = input("재료 타입을 입력하시오: ")

        total_cost = calculate_material_cost(area_py, material_type)

        print(f"방의 평수: {area_py}평")
        print(f"{material_type}의 재료 비용: {total_cost:,}원")

    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()