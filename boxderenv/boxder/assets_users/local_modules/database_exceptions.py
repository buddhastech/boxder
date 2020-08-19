def exception_db_response(response, departments, render_object):
        
        context['response'] = response 
        context['departments'] = departments
        return render_object