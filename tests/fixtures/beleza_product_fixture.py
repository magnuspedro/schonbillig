class BelezaProductFixture:

    def __init__(self, name, price, brand, brand_line, hair_type, size_unit, utility, hair_shaft_condition, texture):
        self.name = name
        self.price = price
        self.brand = brand
        self.brand_line = brand_line
        self.hair_type = hair_type
        self.size_unit = size_unit
        self.utility = utility
        self.hair_shaft_condition = hair_shaft_condition
        self.texture = texture

    def __str__(self):
        string = '''<h1 class="nproduct-title">
                ''' + self.name + '''
                    <span class="product-subtitle">  - Shampoo 50ml</span>
            </h1>
        <div class="product-sku">
                    <strong>Cod: </strong>52110
                </div>
        <div class="container-padding product-datasheet container-padding-top card-xs">
            <div class="accordion-gradient">
                <input type="checkbox" class="is-hide accordion-state" id="product-datasheet" checked="">
                <div class="accordion-gradient-content datasheet">
                    <div class="datasheet-categories"> 
                        <span class="info-label">Categorias</span>
                        <div>
                            <span class="info-link info-link-category">
                                <a href="/cabelos" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet department&quot;, &quot;values&quot;: &quot;department;cabelos&quot;}">
                                    Cabelos
                                </a>
                            </span>
                                <span class="info-link info-link-category">
                                    <a href="/cabelos/shampoo" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet category&quot;, &quot;values&quot;: &quot;category;cabelos/shampoo&quot;}">
                                        Shampoo
                                    </a>
                                </span>
                        </div>
                    </div>
                    <div class="datasheet-characteristics">
                                <div class="info-line">
                                    <span class="info-label">Tipos de Cabelo</span>
                                                <strong class="info-link">
                                                    <a href="/cabelos/shampoo/danificados" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados&quot;}">
                                                        ''' + self.hair_type + '''
                                                    </a>
                                                </strong>       
                                </div>
                                <div class="info-line">
                                    <span class="info-label">Condição dos Fios</span>
                                                <strong class="info-link">
                                                    <a href="/cabelos/shampoo/danificados?condicao-dos-fios=quebradicos" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados?condicao-dos-fios=quebradicos&quot;}">
                                                        ''' + self.hair_shaft_condition + '''
                                                    </a>
                                                </strong>
                                </div>
                                <div class="info-line">
                                    <span class="info-label">Desejo de Beleza</span>
                                                <span class="info-value">
                                                    ''' + self.utility + '''
                                                </span>
                                </div>
                                <div class="info-line">
                                    <span class="info-label">Textura</span>
                                                <span class="info-value">
                                                    ''' + self.texture + '''
                                                </span>
                                </div>
                                <div class="info-line">
                                    <span class="info-label">Tamanho</span>
                                                <strong class="info-link">
                                                    <a href="/cabelos/shampoo/danificados?tamanho=miniatura" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados?tamanho=miniatura&quot;}">
                                                        ''' + self.size_unit + '''
                                                    </a>
                                                </strong>
                               </div>                  
                            <div class="info-line">
                                <span class="info-label">Marca</span>
                                <strong class="info-link">
                                    <a href="/wella-professionals/cabelos/shampoo" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet brand wella-professionals/cabelos/shampoo&quot;}">
                                        ''' + self.brand + '''
                                    </a>
                                </strong>
                            </div>
                            <div class="info-line">
                                <span class="info-label">Linha</span>
                                <strong class="info-link">
                                    <a href="/wella-professionals/fusion" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet brand line wella-professionals/fusion&quot;}">
                                        ''' + self.brand_line + '''
                                    </a>
                                </strong>
                            </div>
                            <div class="info-line">
                                <span class="info-label">Produtos para</span>                                        
                                            <strong class="info-link">
                                                <a href="/cabelos/leave-in-e-creme-para-pentear/normais-e-todos-os-tipos?produtos-para=maciez-e-desembaraco" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/leave-in-e-creme-para-pentear/normais-e-todos-os-tipos?produtos-para=maciez-e-desembaraco&quot;}">
                                                    Maciez e Desembaraço
                                                </a>
                                            </strong>
                                            <strong class="info-link">
                                                <a href="/cabelos/leave-in-e-creme-para-pentear/normais-e-todos-os-tipos?produtos-para=reparacao-de-danos" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/leave-in-e-creme-para-pentear/normais-e-todos-os-tipos?produtos-para=reparacao-de-danos&quot;}">
                                                    Reparação de Danos
                                                </a>
                                            </strong>
                            </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="nprodct-price">     
            <strong class="nproduct-price-max">
                <s>R$ 555.059,90</s>
    <span class="" data-href="https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/">
        (17% de desconto)
    </span>
            </strong>
        <div class="nproduct-price-value" content="49.9">
            R$ ''' + self.price + '''
        </div>
    </div>'''
        return string
