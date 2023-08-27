pipeline{

  agents any
  stages{
    stage('check requirements'){
        setps{
            sh ''' 
                docker --version
                docker compose --version
                curl --version
            '''
        }
    }

    stage('run contianers'){
        sh 'docker compose up -d --no-color'
    }

    stage('testing'){
        sh 'curl http://localhost:8000 > '
    }
  }
 
  post{
    always{
        sh 'docker compose down --remove-orphans -v'
        sh 'docker compose ps'
    }
  }
}