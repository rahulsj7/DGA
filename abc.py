import tkinter as DGA_ANALYSIS
from tkinter import messagebox

def dga(ch4, c2h6, c2h4, c2h2, co, co2):
    """
    Calculates the dissolved gas analysis (DGA) of a transformer oil sample.

    Args:
        ch4: The concentration of methane in parts per million (ppm).
        c2h6: The concentration of ethane in ppm.
        c2h4: The concentration of ethylene in ppm.
        c2h2: The concentration of acetylene in ppm.
        co: The concentration of carbon monoxide in ppm.
        co2: The concentration of carbon dioxide in ppm.

    Returns:
        The DGA results as a dictionary.
    """
    results = {}
    results["CH4"] = ch4
    results["C2H6"] = c2h6
    results["C2H4"] = c2h4
    results["C2H2"] = c2h2
    results["CO"] = co
    results["CO2"] = co2

    # Calculate the total hydrocarbon content.
    total_hydrocarbons = ch4 + 2 * c2h6 + 3 * c2h4 + 4 * c2h2

    # Calculate the hydrogen content.
    hydrogen = total_hydrocarbons - 2 * co - 3 * co2

    # Calculate the oxygen content.
    oxygen = total_hydrocarbons - hydrogen

    results["Total Hydrocarbons"] = total_hydrocarbons
    results["Hydrogen"] = hydrogen
    results["Oxygen"] = oxygen

    # Calculate the fault type.
    fault_type = ""
    if hydrogen > 1000:
        fault_type = "Arcing,Corona Fault code: F3 AND F4"
    elif c2h4 > 100 or co > 1000 or co2>15000:
        fault_type = "Severe Overheating or Arcing Fault code: F3"
    elif c2h6 > 35:
        fault_type = "Local overheating Fault code: F1"
    elif ch4 > 80:
        fault_type = "Sparking Fault code: F2"
    else:
        fault_type = "Normal Fault code: F5"

    results["Fault Type"] = fault_type

    return results

def calculate():
    try:
        # Get the values from the entry fields and convert them to floats
        ch4 = float(ch4_entry.get())
        c2h6 = float(c2h6_entry.get())
        c2h4 = float(c2h4_entry.get())
        c2h2 = float(c2h2_entry.get())
        co = float(co_entry.get())
        co2 = float(co2_entry.get())

        # Call the dga function to calculate the results
        results = dga(ch4, c2h6, c2h4, c2h2, co, co2)

        # Display the results in a messagebox
        result_text = "\n".join(f"{key}: {value}" for key, value in results.items())
        messagebox.showinfo("DGA Results", result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def main():
    global ch4_entry, c2h6_entry, c2h4_entry, c2h2_entry, co_entry, co2_entry

    # Create the root window.
    root = DGA_ANALYSIS.Tk()

    # Create the widgets.
    ch4_entry = DGA_ANALYSIS.Entry(root)
    c2h6_entry = DGA_ANALYSIS.Entry(root)
    c2h4_entry = DGA_ANALYSIS.Entry(root)
    c2h2_entry = DGA_ANALYSIS.Entry(root)
    co_entry = DGA_ANALYSIS.Entry(root)
    co2_entry = DGA_ANALYSIS.Entry(root)

    # Create the labels.
    ch4_label = DGA_ANALYSIS.Label(root, text="CH4 (ppm)")
    c2h6_label = DGA_ANALYSIS.Label(root, text="C2H6 (ppm)")
    c2h4_label = DGA_ANALYSIS.Label(root, text="C2H4 (ppm)")
    c2h2_label = DGA_ANALYSIS.Label(root, text="C2H2 (ppm)")
    co_label = DGA_ANALYSIS.Label(root, text="CO (ppm)")
    co2_label = DGA_ANALYSIS.Label(root, text="CO2 (ppm)")

    # Add the widgets to the window.
    ch4_entry.grid(row=0, column=0)
    c2h6_entry.grid(row=1, column=0)
    c2h4_entry.grid(row=2, column=0)
    c2h2_entry.grid(row=3, column=0)
    co_entry.grid(row=4, column=0)
    co2_entry.grid(row=5, column=0)
    ch4_label.grid(row=0, column=1)
    c2h6_label.grid(row=1, column=1)
    c2h4_label.grid(row=2, column=1)
    c2h2_label.grid(row=3, column=1)
    co_label.grid(row=4, column=1)
    co2_label.grid(row=5, column=1)

    # Create the button.
    calculate_button = DGA_ANALYSIS.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(row=6, column=0, columnspan=2)

    # Start the main event loop.
    root.mainloop()

# Call the main function to run the application.
if __name__ == "__main__":
    main()
