[1mdiff --cc todolist.py[m
[1mindex 67c418e,972b596..0000000[m
[1m--- a/todolist.py[m
[1m+++ b/todolist.py[m
[36m@@@ -45,7 -45,7 +45,11 @@@[m [mif st.session_state.tasks[m
          for t in (st.session_state.tasks):[m
              st.write(f"{t}")   [m
  [m
[32m++<<<<<<< HEAD[m
[32m +#Delete  fff mainaa rrr[m
[32m++=======[m
[32m+ #Delete  fff mainaa       ffffffffffffffffff[m
[32m++>>>>>>> revertb[m
  st.header("Delete Task")[m
  if st.session_state.tasks:[m
      del_index = st.selectbox("Select task index to delete", range(len(st.session_state.tasks)))[m
