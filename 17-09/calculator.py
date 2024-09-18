from datetime import datetime, timedelta

class WorkHourCalculator:

    def _parse_time(self, time_str):
        """Converte uma string de horário no formato HH:mm ou HHmm para um objeto datetime."""
        if len(time_str) == 4 and time_str.isdigit():
            time_str = f"{time_str[:2]}:{time_str[2:]}"
        return datetime.strptime(time_str, "%H:%M")

    def calculate_hours(self, start, end, lunch_break="00:00"):
        """Calcula o total de horas trabalhadas, descontando o intervalo de almoço."""
        try:
            start_time = self._parse_time(start)
            end_time = self._parse_time(end)
            lunch_duration = self._parse_time(lunch_break) - datetime.strptime("00:00", "%H:%M")
        except ValueError:
            raise ValueError("Invalid time format. Expected HH:mm or HHmm.")
        
        if end_time < start_time:
            end_time += timedelta(days=1)

        total_time = end_time - start_time

        total_hours = total_time.total_seconds() / 3600.0

        lunch_duration_hours = lunch_duration.total_seconds() / 3600.0

        total_hours -= lunch_duration_hours

        return round(max(total_hours, 0), 2)
