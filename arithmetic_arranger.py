def arithmetic_arranger(problems, solve = False):
  top = ''
  bottom=''
  lines=''
  solution_item=''
  output=""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
   
    first_number= problem.split(" ")[0]
    second_number=problem.split(" ")[2]
    operator = problem.split(" ")[1]
    
    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if len(first_number) >=5 or len(second_number) >=5:
      return "Error: Numbers cannot be more than four digits."

    if not first_number.isnumeric() or not second_number.isnumeric():
      return "Error: Numbers must only contain digits."

    
    if (operator) == "+":
      answer = str(int(first_number) + int(second_number))
    elif (operator =="-"):
      answer = str(int(first_number) - int(second_number))
   
 
    distance = (  max(len(first_number),len(second_number)) +2)
    

    top_item = str(first_number).rjust(distance)
    
    bottom_item =(operator)+ str(second_number).rjust(distance-1)
    res= answer.rjust(distance)
    line= ""
   

    
    for s in range(distance):
      line += "-" 
    if problem != problems[-1]: 
       
      top += top_item + "    "
      bottom +=bottom_item + "    "
      lines += line+"    "
      solution_item+=res+ "    "
    else:
      top += top_item 
      bottom +=bottom_item 
      lines +=line
      solution_item+=res
      
  if solve : 
    output = top +"\n"+bottom+"\n"+lines+"\n"+solution_item
  else:
    output = top +"\n"+bottom+"\n"+lines
  print(output)
  return output
