from typing import List, Dict, Callable, Any

def aggregate_data(data: List[Dict[str, Any]], group_key: str, aggregator: Callable[[List[Any]], Any]) -> Dict[str, Any]:
    """
    Aggregates data by grouping items based on a specified key and applying an aggregation function to each group.
    """

    grouped_data = {}
    
    for item in data:
        key = item[group_key]
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(item['value'])
    
    aggregated_data = {k: aggregator(v) for k, v in grouped_data.items()}
    
    return aggregated_data


data = [
    {'category': 'fruit', 'value': 10},
    {'category': 'fruit', 'value': 20},
    {'category': 'vegetable', 'value': 30},
    {'category': 'vegetable', 'value': 40}
]

def sum_aggregator(values):
    """
    Aggregates the sum of a list of values.
    """

    return sum(values)

result = aggregate_data(data, 'category', sum_aggregator)
print(result)  